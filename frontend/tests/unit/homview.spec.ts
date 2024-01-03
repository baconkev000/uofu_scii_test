// Import Vue Test Utils and the component being tested
import { mount } from "@vue/test-utils";
import HomeView from "@/views/HomeView.vue";

import players from "@/fixtures/players.json";
import attrs from "@/fixtures/attributes.json";
import axios from "axios";

// Mock Axios
jest.mock("axios");

describe("HomeView.vue", () => {
  it("renders correctly", async () => {
    // Mock data for testing
    const mockPlayers = players;

    const mockAttributes = attrs;

    // Mock Axios response
    (axios.get as jest.Mock).mockResolvedValueOnce({ data: mockPlayers });
    (axios.get as jest.Mock).mockResolvedValueOnce({ data: mockAttributes });

    // Mount the component
    const wrapper = mount(HomeView);

    // Wait for async data to be fetched
    await wrapper.vm.$nextTick();

    // Check if the component renders correctly
    expect(wrapper.html()).toMatchSnapshot();
  });
});
