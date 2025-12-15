import { render, screen } from "@testing-library/react";
import { useRiders } from "../hooks/useRiders";
import Riders from "./Riders";
import { vi } from "vitest";

vi.mock("../hooks/useRiders");

describe("Riders component", () => {
  it("renders loading state", () => {
    (useRiders as any).mockReturnValue({
      riders: [],
      loading: true,
      error: null,
    });
    render(<Riders />);
    expect(screen.getByText(/Loading riders.../i)).toBeInTheDocument();
  });

  it("renders error state", () => {
    (useRiders as any).mockReturnValue({
      riders: [],
      loading: false,
      error: "Error loading riders",
    });
    render(<Riders />);
    expect(screen.getByText(/Error loading riders/i)).toBeInTheDocument();
  });

  it("renders riders list", () => {
    const mockRiders = [
      {
        id: 1,
        name: "Maverick",
        surname: "Viñales",
        number: 12,
        country: "ES",
      },
      { id: 2, name: "Johann", surname: "Zarco", number: 5, country: "FR" },
    ];
    (useRiders as any).mockReturnValue({
      riders: mockRiders,
      loading: false,
      error: null,
    });
    render(<Riders />);

    expect(screen.getByText(/Maverick Viñales/i)).toBeInTheDocument();
    expect(screen.getByText(/Johann Zarco/i)).toBeInTheDocument();
  });
});
