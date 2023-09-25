class Rocket:
    def __init__(self):
        self.stage = "Pre-Launch"
        self.fuel = 100
        self.altitude = 0
        self.speed = 500

    def update(self, seconds):
        if self.stage == "Pre-Launch":
            print("Rocket is still in Pre-Launch stage. Initiate launch to proceed.")
            return

        if self.fuel <= 0:
            print("Mission Failed due to insufficient fuel.")
            return

        self.altitude += self.speed * seconds
        self.fuel -= seconds
        print(f"Stage: {self.stage}, Fuel: {self.fuel}%, Altitude: {self.altitude} km, Speed: {self.speed} km/h")

    def stage_separation(self):
        if self.stage == "Pre-Launch":
            print("Rocket is still in Pre-Launch stage. Initiate launch to proceed.")
            return

        print(f"Stage {self.stage} complete. Separating stage. Entering Stage {int(self.stage) + 1}.")
        self.stage = str(int(self.stage) + 1)
        self.fuel = 100
        self.speed += 100

class Simulator:
    def __init__(self):
        self.rocket = Rocket()

    def start_checks(self):
        if self.rocket.stage == "Pre-Launch":
            print("All systems are 'Go' for launch.")
        else:
            print("Rocket is already in flight. Cannot perform pre-launch checks.")

    def launch(self):
        if self.rocket.stage == "Pre-Launch":
            self.rocket.stage = "1"
            print("Rocket launch initiated.")
        else:
            print("Rocket is already in flight. Cannot launch again.")

    def fast_forward(self, seconds):
        if self.rocket.stage == "Pre-Launch":
            print("Rocket is still in Pre-Launch stage. Initiate launch to proceed.")
            return

        for _ in range(seconds):
            self.rocket.update(1)
            if self.rocket.altitude >= 10000:  # Example: Orbit placement at 1000 km altitude
                print("Orbit achieved! Mission Successful.")
                return
            elif self.rocket.altitude >= 5000:
                self.rocket.stage_separation()
                break

    def run_simulation(self):
        while True:
            user_input = input("Enter a command: ")
            if user_input == "start_checks":
                self.start_checks()
            elif user_input == "launch":
                self.launch()
            elif user_input.startswith("fast_forward"):
                try:
                    _, seconds = user_input.split()
                    self.fast_forward(int(seconds))
                except ValueError:
                    print("Invalid input. Use 'fast_forward X' where X is an integer.")
            else:
                print("Invalid command. Please enter 'start_checks', 'launch', or 'fast_forward X'.")

if __name__ == "__main__":
    simulator = Simulator()
    simulator.run_simulation()
