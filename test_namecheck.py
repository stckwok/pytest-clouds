from namecheck import logic
from click.testing import CliRunner
from namecheck import marco


def test_marco_polo():
    runner = CliRunner()
    result = runner.invoke(marco, ["--name", "Marco"])
    assert result.exit_code == 0
    assert "Polo" in result.output


def test_marco_bob():
    runner = CliRunner()
    result = runner.invoke(marco, ["--name", "Bob"])
    assert result.exit_code == 0
    assert "No Match" in result.output


def test_logic():
    assert "Polo" in logic("Marco")
    assert "No Match" == logic("Bob")
