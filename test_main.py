def test_program_runs():
try:
import main
assert True
except Exception:
assert False, "Your program has an error and could not run"
