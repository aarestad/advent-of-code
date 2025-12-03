## advent of code 2023
## https://adventofcode.com/2023
## day 20

from dataclasses import dataclass
from enum import Enum, auto
from abc import ABC, abstractmethod
from typing import List, Dict
import re


class Signal(Enum):
    HIGH = auto()
    LOW = auto()

    def __invert__(self) -> "Signal":
        return Signal.LOW if self == Signal.HIGH else Signal.HIGH


class Module(ABC):
    name: str
    receivers: List["Module"] = []

    @abstractmethod
    def process(self, signal: Signal, sender: "Module"): ...

    @abstractmethod
    def send(self): ...


class FlipFlop(Module):
    state: Signal = Signal.LOW
    flipped: bool = False

    def process(self, signal: Signal, _sender: "Module"):
        if signal == Signal.LOW:
            self.state = ~self.state
            self.flipped = True

    def send(self):
        if self.flipped:
            for r in self.receivers:
                r.recv(self.state, self)
            for r in self.receivers:
                r.send()


class Conjunction(Module):
    memory: Dict[str, Signal] = {}

    def process(self, signal: Signal, sender: Module):
        self.memory[sender.name] = signal

    def send(self):
        sent = (
            Signal.LOW
            if all(s == Signal.HIGH for s in self.memory.values())
            else Signal.HIGH
        )

        for r in self.receivers:
            print(f"{self.name} -{str(self.signal).lower()}-> {r.name}")
            r.process(sent, self)

        for r in self.receivers:
            r.send(sent)


class Broadcaster(Module):
    signal: Signal = None

    def process(self, signal: Signal, _sender: Module):
        self.signal = signal

    def send(self):
        for r in self.receivers:
            print(f"{self.name} -{str(self.signal).lower()}-> {r.name}")
            r.process(self.signal, self)

        for r in self.receivers:
            r.send(self.signal)


class Button(Module):
    def send(self):
        for r in self.receivers:
            print(f"{self.name} -{str(self.signal).lower()}-> {r.name}")
            r.process(self.signal, self)

        for r in self.receivers:
            r.send(self.signal)


def parse_input(lines):
    module_links: Dict[str, List[str]] = {}
    conn_parser = re.compile(r"(\w+) -> (.+)")

    for l in lines:
        if not l:
            continue

        parsed = conn_parser.search(l)
        name = parsed[1]
        links = [s.strip() for s in parsed[2].split(",")]

        # &hf -> rg, vl, tq, qq, mv, zz
        if l.startswith("%"):
            type = "FlipFlop"
        elif l.startswith("&"):
            type = "Conjunction"
        elif l.startswith("broadcaster"):
            type = ""
        else:
            raise ValueError(f"can't figure out type for line {l}")

        module_links[f"{name}|{type}"] = links

    button = Button("button")
    broadcaster = Broadcaster("broadcaster")
    button.receivers.append(broadcaster)

    created_modules = {}
    created_modules[button.name] = button
    created_modules[broadcaster.name] = broadcaster

    current_module = broadcaster
    links = module_links["broadcaster|"]
    del module_links["broadcaster|"]

    while links:
        for link in links:
            name, type = link.split("|")

            if name in created_modules:
                mod = created_modules[name]
            elif type == "FlipFlop":
                mod = FlipFlop(name)
            elif type == "Conjunction":
                mod = Conjunction(name)
            else:
                raise ValueError(f"bad type: {type}")

            current_module.receivers.append(mod)

            if not name in created_modules:
                created_modules[name] = mod


def part1(data):
    pass


def part2(data):
    pass
