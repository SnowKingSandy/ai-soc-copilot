import React from "react";
import { render, screen } from "@testing-library/react";
import InvestigationReport from "../InvestigationReport";

describe("InvestigationReport", () => {
  it("renders report fields", () => {
    const mock = {
      timeline: "t1",
      root_cause: "rc",
      attack_chain: "ac",
      recommended_actions: ["a1", "a2"],
    };

    render(<InvestigationReport report={mock} />);

    expect(screen.getByText(/Investigation Report/i)).toBeInTheDocument();
    expect(screen.getByText(/t1/)).toBeInTheDocument();
    expect(screen.getByText(/rc/)).toBeInTheDocument();
    expect(screen.getByText(/ac/)).toBeInTheDocument();
    expect(screen.getByText(/a1/)).toBeInTheDocument();
  });
});
