from gym.envs.registration import register

register(
    id="gym_examples/DangerousDave-v0",
    entry_point="gym_examples.envs:DangerousDaveEnv",
)
