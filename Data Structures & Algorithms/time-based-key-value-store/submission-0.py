class TimeMap:

    def __init__(self):
        self.status = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.status:
            self.status[key] = {}
        
        if timestamp not in self.status:
            self.status[key][timestamp] = []
        
        self.status[key][timestamp].append(value)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.status:
            return ""
        seen = 0

        for time in self.status[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.status[key][seen][-1]
