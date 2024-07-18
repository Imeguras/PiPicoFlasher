Import("env")
# Multiple actions
env.AddCustomTarget(
    name="joao_faz_o_flash",
    dependencies=None,
    actions=[
        "cp .pio/build/pico/firmware.uf2 /media/$USER/RPI-RP2"
    ],
    title="Joao Faz o Flash",
    description="Faz o flash do raspberry pi pico "
)