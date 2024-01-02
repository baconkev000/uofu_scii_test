<template>
  <div class="w-full flex justify-center items-center">
    <div class="relative overflow-x-auto shadow-md">
      <table class="w-full text-sm text-left rtl:text-right text-black">
        <thead class="text-xs text-gray-700 uppercase bg-gray-600 text-white">
          <tr>
            <th v-for="row in t_rows" :key="row" scope="col" class="px-6 py-3">
              {{ row }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            class="bg-white border-b bg-slate-200 even:bg-gray-100 odd:bg-gray-200 hover:bg-white cursor-pointer"
            v-for="player in players"
            :key="player.pk"
          >
            <th
              scope="row"
              class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap font-bold"
            >
              {{ player.fields.Name }}
            </th>
            <td class="px-6 py-4">
              {{
                player.fields.Nationality ? player.fields.Nationality : "N/A"
              }}
            </td>
            <td class="px-6 py-4">
              {{
                player.fields.National_Position
                  ? player.fields.Nationality
                  : "N/A"
              }}
            </td>
            <td class="px-6 py-4">
              {{ player.fields.Club ? player.fields.Club : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.fields.Height ? player.fields.Height : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{
                player.fields.Preffered_Foot
                  ? player.fields.Preffered_Foot
                  : "N/A"
              }}
            </td>
            <td class="px-6 py-4">
              {{
                player.fields.Ball_Control ? player.fields.Ball_Control : "N/A"
              }}
            </td>
            <td class="px-6 py-4">
              {{ player.fields.Dribbling ? player.fields.Dribbling : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.fields.Vision ? player.fields.Vision : "N/A" }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
import { APIService } from "@/services/api";
import type { Player } from "@/types/player";
import { ref } from "vue";
import fixture from "@/fixture.json";

export default class HomeView extends Vue {
  t_rows = ref([
    "Name",
    "Nationality",
    "National Position",
    "Club",
    "Height",
    "Preferred Foot",
    "Ball Control",
    "Dribbling",
    "Vision",
  ] as string[]);
  info = ref();
  loading = ref(true);

  data() {
    return {
      players: fixture,
    };
  }

  // mounted() {
  //   APIService.getPlayers()
  //     .then((response: any) => (this.players = response.data))
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }
}
</script>
