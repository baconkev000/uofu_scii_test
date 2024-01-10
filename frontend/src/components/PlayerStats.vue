<template>
  <div class="py-24 w-full overflow-x-auto flex flex-col justify-center">
    <h2 class="text-2xl font-semibold p-4 underline">Player Stats</h2>
    <div class="grid grid-cols-3 gap-2 text-left divide-white">
      <div v-for="statName in Object.keys(player)" :key="statName">
        <span class="font-semibold">{{ statName }}:</span>{{ player[statName] }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import type { PlayerFields } from "@/types/player_fields";
@Options({
  props: {
    player: Object as () => PlayerFields,
  },
})
export default class PlayerStats extends Vue {
  player!: PlayerFields;
}
</script>
