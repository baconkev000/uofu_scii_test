<template>
  <div
    class="py-24 w-full overflow-x-auto border-2 border-slate-300 bg-slate-200"
  >
    <h2>{{ selectedLabel }}</h2>
    <svg id="myPlot" class="border-2 border-slate-500 overflow-x-auto"></svg>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import type { PlayerFields } from "@/types/player_fields";
import { Watch } from "vue-property-decorator";
import num_labels from "@/fixtures/labels/numerical.json";
import * as d3 from "d3";
@Options({
  props: {
    players: Array as () => PlayerFields[],
    selectedLabel: String,
    num_labels: Array as () => string[],
    cat_labels: Array as () => string[],
  },
})
export default class PlayerVisuals extends Vue {
  players!: PlayerFields[];
  selectedLabel!: keyof PlayerFields;
  width = 1000;
  height = 600;
  margin = 40;
  marginTop = 30;
  marginRight = 0;
  marginBottom = (this.height - this.margin) / 2;
  marginLeft = 50;
  xMax = this.width - this.margin * 2;
  yMax = this.height / 1.5 - this.margin * 2;

  updateChart() {
    const svg = d3
      .select("#myPlot")
      .attr("viewBox", `0 -${this.margin} ${this.width} ${this.height}`);

    svg.selectAll("*").remove(); // Clear existing chart

    if (this.players.length > 0) {
      this.createChart(svg);
    }
  }

  createChart(svg: any) {
    let cleanedPlayerData!: unknown[];
    let maxYTick = 0;
    let yAxisLabel = "";

    if (num_labels.find((label: string) => label === this.selectedLabel)) {
      cleanedPlayerData = this.players.map((p: PlayerFields) => ({
        name: p.Name,
        numeric: p[this.selectedLabel] ? p[this.selectedLabel] : 0,
      }));
      yAxisLabel = `${this.selectedLabel} Stats`;
    } else {
      const uniqueLabelVals = Array.from(
        new Set(
          this.players.map((p: PlayerFields) => {
            return p[this.selectedLabel] ? p[this.selectedLabel] : "N/A";
          })
        )
      );
      cleanedPlayerData = uniqueLabelVals.map((uVal: any) => ({
        name: uVal,
        numeric: this.players.filter(
          (player: PlayerFields) => player[this.selectedLabel] === uVal
        ).length,
      }));
      yAxisLabel = `# of Players - ${this.selectedLabel}`;
    }
    maxYTick = Math.max(...cleanedPlayerData.map((p: any) => p.numeric));
    console.log(maxYTick, cleanedPlayerData);
    const x = d3
      .scaleBand()
      .domain(
        d3.groupSort(
          cleanedPlayerData,
          ([d]: any) => -d.numeric,
          (d: any) => d.name
        )
      ) // descending frequency
      .range([0, this.xMax]);

    const y = d3
      .scaleLinear()
      .domain([0, d3.max(cleanedPlayerData, (d: any) => d.numeric)])
      .range([this.yMax, 0]);

    const colorScale = d3.scaleOrdinal(d3.schemeCategory10);
    svg
      .append("g")
      .attr("transform", `translate(${this.marginLeft},0)`)
      .selectAll()
      .data(cleanedPlayerData)
      .join("rect")
      .attr("x", (d: any) => x(d.name))
      .attr("y", (d: any) => y(d.numeric))
      .attr("height", (d: any) => y(0) - y(d.numeric))
      .attr("width", x.bandwidth())
      .attr("fill", (_d: any, i: number) => colorScale(i.toString())); // Convert index to string

    // Add the x-axis and label.
    svg
      .append("g")
      .attr(
        "transform",
        `translate(${this.marginLeft},${this.height - this.marginBottom})`
      )
      .call(d3.axisBottom(x).tickSizeOuter(0))
      .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-0.8em")
      .attr("dy", "0.15em")
      .attr("transform", "rotate(-45)");

    // Add the y-axis and label, and remove the domain line.
    svg
      .append("g")
      .attr("transform", `translate(${this.marginLeft},0)`)
      .call(
        d3
          .axisLeft(y)
          .ticks(Math.min(maxYTick, 15))
          .tickFormat((y: any) =>
            (
              (y * maxYTick) /
              d3.max(cleanedPlayerData, (d: any) => d.numeric)
            ).toFixed()
          )
      )
      .call((g: any) => g.select(".domain").remove())
      .call((g: any) =>
        g
          .append("text")
          .attr("x", -this.marginLeft)
          .attr("y", -10)
          .attr("fill", "currentColor")
          .attr("text-anchor", "start")
          .text(`↑ ${yAxisLabel}`)
      );
  }

  @Watch("selectedLabel")
  @Watch("players")
  async onPlayersChange() {
    this.updateChart();
  }

  mounted() {
    this.onPlayersChange();
  }
}
</script>

<style scoped>
/* Add your styles here */
</style>
