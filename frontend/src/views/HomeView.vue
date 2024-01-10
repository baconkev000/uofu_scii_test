<template>
  <div class="w-full flex space-between bg-slate-300 lg:flex-row flex-col">
    <div
      class="xl:w-1/2 w-full xl:flex-col flex-row px-4 h-max overflow-x-scroll"
    >
      <!-- Dropdown -->
      <div class="flex flex-row justify-end w-full py-8">
        <div class="relative inline-block text-left">
          <div>
            <button
              type="button"
              class="inline-flex w-full justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
              id="menu-button"
              aria-expanded="true"
              aria-haspopup="true"
              @click="toggleDropdown()"
            >
              Attributes
              <svg
                class="-mr-1 h-5 w-5 text-gray-400"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </div>
          <div
            v-show="isDropdownOpen"
            @click="toggleDropdown"
            class="fixed inset-0 bg-black opacity-25 z-9"
          ></div>
          <div
            v-show="isDropdownOpen"
            class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
            role="menu"
            aria-orientation="vertical"
            aria-labelledby="menu-button"
            tabindex="-1"
          >
            <div class="py-1" role="none">
              <label
                v-for="attribute in attributes"
                :key="attribute"
                class="flex items-center px-4 py-2 text-sm"
              >
                <input
                  type="checkbox"
                  :value="attribute"
                  v-model="selectedAttributes"
                  class="mr-2"
                  @click="updateAttrs(attribute)"
                />
                {{ attribute }}
              </label>
            </div>
          </div>
        </div>
      </div>
      <!-- Table -->
      <div
        class="w-full mx-auto overflow-x-auto overflow-y-auto h-screen shadow-lg"
      >
        <table class="w-full text-sm text-center rtl:text-right text-black">
          <thead class="text-xs text-gray-700 uppercase bg-gray-600 text-white">
            <tr>
              <th
                @click="updateSorted('Name')"
                scope="col"
                class="px-6 py-3 cursor-pointer"
              >
                Name
              </th>
              <th
                v-for="row in selectedAttributes"
                :key="row"
                @click="updateSorted(row)"
                scope="col"
                class="px-6 py-3 cursor-pointer"
              >
                {{ row }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="bg-white border-b bg-slate-200 even:bg-gray-100 odd:bg-gray-200 hover:bg-white cursor-pointer"
              v-for="player in sortedPlayers"
              :key="player.pk"
            >
              <td
                scope="row"
                class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap font-medium"
                @click="getSelectedPlayer(player.Name)"
              >
                {{ player.Name }}
              </td>
              <td
                v-for="attr in selectedAttributes"
                :key="attr"
                class="px-6 py-4"
              >
                {{ player[attr] ? player[attr] : "N/A" }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div
      class="lg:w-1/2 w-full flex flex-col justify-center items-center bg-slate-200 px-4"
    >
      <PlayerStats
        v-if="showPlayerStats"
        :player="selectedPlayer"
      ></PlayerStats>
      <PlayerVisuals
        v-else
        :players="sortedPlayers"
        :selectedLabel="selectedLabel"
      ></PlayerVisuals>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import { APIService } from "@/services/api";
import PlayerVisuals from "@/components/PlayerVisual.vue";
import PlayerStats from "@/components/PlayerStats.vue";
import { PlayerFields } from "@/types/player_fields";

@Options({
  components: {
    PlayerVisuals,
    PlayerStats,
  },
})
export default class HomeView extends Vue {
  selectedAttributes: string[] = [
    "Nationality",
    "National_Position",
    "Club",
    "Height",
    "Preffered_Foot",
    "Ball_Control",
    "Dribbling",
    "Vision",
  ];
  sortedPlayers: PlayerFields[] = [];
  attributes: string[] = [];
  isDropdownOpen = false;
  selectedLabel = "Rating";
  showPlayerStats = false;
  selectedPlayer: any = {};

  toggleDropdown() {
    this.isDropdownOpen = !this.isDropdownOpen;
  }

  updateAttrs(attr: string): void {
    const index = this.selectedAttributes.indexOf(attr);

    if (index !== -1) {
      // If the attribute is already selected, remove it
      this.selectedAttributes.splice(index, 1);
    } else {
      // If the attribute is not selected, add it
      this.selectedAttributes.push(attr);
    }
  }

  updateSorted(header: string): void {
    this.selectedLabel = header !== "Name" ? header : "Rating";
    this.showPlayerStats = false;
    header = header.split(" ").join("_");
    this.sortedPlayers = this.sortedPlayers.sort(
      (playerA: PlayerFields, playerB: PlayerFields) => {
        const aValue = playerA[header as keyof typeof playerA];
        const bValue = playerB[header as keyof typeof playerA];

        const compareValues = (aValue: any, bValue: any): number => {
          // If both values are null, consider them equal
          if (aValue === null && bValue === null) {
            return 0;
          }

          // If only aValue is null, prioritize it to the bottom
          if (aValue === null) {
            return 1;
          }

          // If only bValue is null, prioritize it to the bottom
          if (bValue === null) {
            return -1;
          }

          // The rest of your comparison logic for non-null values
          return aValue.localeCompare(bValue);
        };

        const compareNumbers = (aValue: number, bValue: number) => {
          return aValue - bValue;
        };

        if (typeof aValue === "string" && typeof bValue === "string") {
          return aValue.localeCompare(bValue);
        } else if (typeof aValue === "number" && typeof bValue === "number") {
          return compareNumbers(aValue, bValue);
        } else {
          return compareValues(aValue, bValue);
        }
      }
    );
  }
  getSelectedPlayer(playerName: string) {
    // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
    this.selectedPlayer = this.sortedPlayers.find(
      (p: PlayerFields) => p.Name === playerName
    )!;
    this.showPlayerStats = true;
  }

  async mounted() {
    // get players
    try {
      const response = await APIService.getPlayers();
      this.sortedPlayers = response.data;
    } catch (error) {
      console.log(error);
    }
    // get attributes
    try {
      const response = await APIService.getAttributes();
      this.attributes = response.data;
    } catch (error) {
      console.log(error);
    }
  }
}
</script>
