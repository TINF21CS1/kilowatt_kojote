import platform

from smartmeter.environment.main import main

if __name__ == "__main__":
    seed = platform.node()
    main(seed)