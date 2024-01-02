<template>
  <div class="home">
    <div class="text-3xl">Hello</div>
    <li v-for="player in players" :key="player.pk" class="text-black text-2xl">
      {{ player.fields.Name }}
    </li>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
import { APIService } from "@/services/api";
import type { Player } from "@/types/player";
import { ref } from "vue";

export default class HomeView extends Vue {
  players = ref();
  info = ref();

  loading = ref(true);

  data() {
    return {
      players: undefined,
    };
  }

  mounted() {
    APIService.getPlayers()
      .then((response: any) => (this.players = response.data))
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>
