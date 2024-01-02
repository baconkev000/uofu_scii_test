<template>
  <div class="w-full flex justify-center items-center flex-col">
    <div class="flex flex-row justify-end w-5/6 py-8">
      <button
        id="dropdownCheckboxButton"
        data-dropdown-toggle="dropdownDefaultCheckbox"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        type="button"
      >
        Dropdown checkbox
        <svg
          class="w-2.5 h-2.5 ms-3"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 10 6"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="m1 1 4 4 4-4"
          />
        </svg>
      </button>

      <!-- Dropdown menu -->
      <div
        id="dropdownDefaultCheckbox"
        class="z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600"
      >
        <ul
          class="p-3 space-y-3 text-sm text-gray-700 dark:text-gray-200"
          aria-labelledby="dropdownCheckboxButton"
        >
          <li>
            <div class="flex items-center">
              <input
                id="checkbox-item-1"
                type="checkbox"
                value=""
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
              />
              <label
                for="checkbox-item-1"
                class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Default checkbox</label
              >
            </div>
          </li>
          <li>
            <div class="flex items-center">
              <input
                checked
                id="checkbox-item-2"
                type="checkbox"
                value=""
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
              />
              <label
                for="checkbox-item-2"
                class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Checked state</label
              >
            </div>
          </li>
          <li>
            <div class="flex items-center">
              <input
                id="checkbox-item-3"
                type="checkbox"
                value=""
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
              />
              <label
                for="checkbox-item-3"
                class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Default checkbox</label
              >
            </div>
          </li>
        </ul>
      </div>
    </div>

    <div class="relative overflow-x-auto shadow-md">
      <table class="w-full text-sm text-left rtl:text-right text-black">
        <thead class="text-xs text-gray-700 uppercase bg-gray-600 text-white">
          <tr>
            <th v-for="row in t_rows" :key="row" scope="col" class="px-6 py-3">
              {{ row }}
            </th>
          </tr>
        </thead>
        <div v-if="loading">Loading...</div>
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
              {{ player.Name }}
            </th>
            <td class="px-6 py-4">
              {{ player.Nationality ? player.Nationality : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.National_Position ? player.Nationality : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.Club ? player.Club : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.Height ? player.Height : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.Preffered_Foot ? player.Preffered_Foot : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.Ball_Control ? player.Ball_Control : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.Dribbling ? player.Dribbling : "N/A" }}
            </td>
            <td class="px-6 py-4">
              {{ player.Vision ? player.Vision : "N/A" }}
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
import type { Ref } from "vue";

export default class HomeView extends Vue {
  t_rows: Ref<string[]> = ref([
    "Name",
    "Nationality",
    "National Position",
    "Club",
    "Height",
    "Preferred Foot",
    "Ball Control",
    "Dribbling",
    "Vision",
  ]);
  loading = ref(true);
  players: Ref<Player[]> = ref([]);

  async mounted() {
    console.log(this.players);
    APIService.getPlayers()
      .then((response) => (this.players = response.data))
      .catch((error) => console.log(error))
      .finally((this.loading = false));
  }
}
</script>
