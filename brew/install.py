from core.process import run_command
from core.formatter import print_status
from brew.tools import taps, formulae, casks

def install():
    print_status("\nTaps:")
    for tap in [tap.strip() for tap in taps.splitlines() if tap.strip()]:
        res = run_command(["brew", "tap", tap])
        print_output(res)

    print_status("\nCasks:")
    for cask in [cask.strip() for cask in casks.splitlines() if cask.strip()]:
        res = run_command(["brew", "install", "--cask", cask])
        print_output(res)

    print_status("\nFormulae:")
    for formula in [formula.strip() for formula in formulae.splitlines() if formula.strip()]:
        output = run_command(["brew", "install", formula])
        print_output(output)

def print_output(output: tuple[bool, str, str]):
    success, stdout, stderr = output
    if success:
        if stdout:
            print(f"✅: {stdout} \n")
        if stderr:  # Handle brew warnings
            print(f"✅: {stderr} \n")
        else:
            print("✅ \n")
    else:
        print(f"❌: {stderr} \n")

