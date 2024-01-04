<template>
  <div>
    <h2>Numerical Skills</h2>
    <canvas ref="numericalChart" class="h-1/2"></canvas>

    <h2>Categorical Variables Skill</h2>
    <canvas ref="categoricalChart"></canvas>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import { Watch } from "vue-property-decorator";
import Chart from "chart.js/auto";
import type { Player } from "@/types/player";

@Options({
  components: {
    Chart,
  },
  props: {
    players: Array,
  },
})
export default class PlayerVisuals extends Vue {
  players!: [];
  playersData: Player[] | null = null;

  @Watch("players")
  async onPlayersChange(newPlayers: Array<any>) {
    if (newPlayers) {
      this.playersData = await newPlayers;
      if (!this.playersData || !this.playersData.length) {
        console.log("No players data available", this.players);
      } else {
        this.createNumericalChart();
        this.createCategoricalChart();
      }
    } else {
      console.warn("Players data not available");
    }
  }

  mounted() {
    this.onPlayersChange(this.players);
  }

  private createNumericalChart() {
    let numericalLabels = Object.keys(this.players[0]).filter(
      (key) => typeof this.players[0][key] === "number"
    );
    numericalLabels = numericalLabels.slice(1);
    numericalLabels = numericalLabels.slice(
      numericalLabels.indexOf("Contract_Expirey")
    );
    const numericalData = this.players.map((player) =>
      numericalLabels.map((label) => player[label] as number)
    );

    const datasets = numericalData.map((data, index) => {
      const randomColor = this.getRandomColor();
      return {
        label: this.players[index].Name,
        data: data.map((value, i) => ({ x: value, y: value })),
        backgroundColor: `rgba(${randomColor.r}, ${randomColor.g}, ${randomColor.b}, 0.2)`,
        borderColor: `rgba(${randomColor.r}, ${randomColor.g}, ${randomColor.b}, 1)`,
        borderWidth: 1,
        pointRadius: 6,
        pointHoverRadius: 8,
      };
    });

    this.createScatterChart(
      "numericalChart",
      numericalLabels,
      datasets,
      "Numerical Skills"
    );
  }

  private getRandomColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return { r, g, b };
  }

  private createCategoricalChart() {
    const categoricalLabels = Object.keys(this.players[0]).filter(
      (key) => typeof this.players[0][key] === "string"
    );

    const categoricalData = this.players.map((player) =>
      categoricalLabels.map((label) => player[label] as string)
    );

    this.createPieChart(
      "categoricalChart",
      categoricalLabels,
      categoricalData,
      "Categorical Skills"
    );
  }

  private createScatterChart(
    canvasRef: string,
    labels: string[],
    datasets: any[],
    title: string
  ) {
    const ctx = (this.$refs[canvasRef] as HTMLCanvasElement).getContext("2d");
    new Chart(ctx, {
      type: "scatter",
      data: {
        labels,
        datasets,
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
          x: {
            beginAtZero: true,
          },
        },
      },
    });
  }

  private createPieChart(
    canvasRef: string,
    labels: string[],
    data: string[],
    title: string
  ) {
    const ctx = (this.$refs[canvasRef] as HTMLCanvasElement).getContext("2d");
    new Chart(ctx, {
      type: "pie",
      data: {
        labels,
        datasets: [
          {
            data,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
    });
  }
}
</script>

<style scoped>
/* Add your styles here */
</style>
