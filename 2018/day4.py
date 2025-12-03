"""2018 Day 4"""

from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime
from typing import Optional
import re


class LogEntryType(Enum):
    """The types of guard log entries"""

    DUTY_START = auto()  # Value = guard ID
    WAKE_UP = auto()
    FALL_ASLEEP = auto()


@dataclass(frozen=True)
class LogEntry:
    """An entry from the guard log"""

    # timestamp of entry
    timestamp: datetime
    # entry type
    type: LogEntryType
    # the most recent guard ID, or the new one if it's a shift change
    guard_id: Optional[int]

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __le__(self, other):
        return self.timestamp <= other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __ge__(self, other):
        return self.timestamp <= other.timestamp

    def __eq__(self, other):
        return self.timestamp == other.timestamp

    def __ne__(self, other):
        return self.timestamp != other.timestamp


log_pattern = re.compile(r"\[(.+)\] (.+)")
shift_start_pattern = re.compile(r"Guard #(\d+) begins shift")

if __name__ == "__main__":
    EXAMPLE = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

    example_input = EXAMPLE.split("\n")

    with open("input/day4.txt", encoding="utf-8") as input:
        problem_input = [i.strip() for i in input.readlines()]

    log_entries = []

    for entry in example_input:
        entry_groups = log_pattern.match(entry).groups()
        timestamp = datetime.strptime(entry_groups[0], "%Y-%m-%d %H:%M")
        message = entry_groups[1]

        type = (
            LogEntryType.FALL_ASLEEP
            if message == "falls asleep"
            else LogEntryType.WAKE_UP
            if message == "wakes up"
            else LogEntryType.DUTY_START
        )

        guard_id = None

        if type == LogEntryType.DUTY_START:
            parsed_message = shift_start_pattern.search(message)
            guard_id = parsed_message[1]

        log_entries.append(LogEntry(timestamp, type, guard_id))

    log_entries.sort(key=lambda e: e.timestamp)

    current_guard = None
    current_sleep_start_time = None

    guard_sleep_times = {}

    for e in log_entries:
        match e.type:
            case LogEntryType.DUTY_START:
                current_guard = e.guard_id

                if current_sleep_start_time is not None:
                    print(f"previous guard {current_guard} is still asleep?")
                    current_sleep_start_time = None

            case LogEntryType.FALL_ASLEEP:
                if current_sleep_start_time is not None:
                    print(f"current guard {current_guard} is already asleep")

                current_sleep_start_time = e.timestamp

            case LogEntryType.WAKE_UP:
                if current_sleep_start_time is None:
                    print(f"current guard {current_guard} is not asleep")

                num_minutes_asleep = (
                    e.timestamp - current_sleep_start_time
                ).total_seconds() / 60

                if current_guard in guard_sleep_times:
                    guard_sleep_times[current_guard] += num_minutes_asleep
                else:
                    guard_sleep_times[current_guard] = num_minutes_asleep

                current_sleep_start_time = None

    print(guard_sleep_times)
