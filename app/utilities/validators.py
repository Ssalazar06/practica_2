from datetime import date

_SSN_MAX_DIGITS = 9


def validate_non_empty_text(value: str, field_name: str) -> tuple[str | None, str | None]:
    """Validate non-empty text input and return normalized value."""
    normalized_value = value.strip()
    return (normalized_value, None) if normalized_value else (None, f"{field_name} no puede estar vacío.")


def validate_ssn(value: str) -> tuple[str | None, str | None]:
    """Validate SSN as digits only, between 1 and nine digits inclusive."""
    normalized_value = value.strip()
    if not normalized_value:
        return None, "El documento no puede estar vacío."
    if not normalized_value.isdigit():
        return None, "El documento debe ser estrictamente numérico."
    return (
        (normalized_value, None)
        if len(normalized_value) <= _SSN_MAX_DIGITS
        else (None, f"El documento admite como máximo {_SSN_MAX_DIGITS} dígitos.")
    )


def validate_positive_salary(value: str) -> tuple[float | None, str | None]:
    """Validate salary as a positive numeric value."""
    try:
        parsed_value = float(value.strip())
        return (parsed_value, None) if parsed_value > 0 else (None, "El salario debe ser mayor que cero.")
    except ValueError:
        return None, "El salario debe ser un valor numérico."


def validate_iso_date(value: str, field_name: str) -> tuple[date | None, str | None]:
    """Validate date using ISO format YYYY-MM-DD."""
    try:
        return date.fromisoformat(value.strip()), None
    except ValueError:
        return None, f"Formato de {field_name} inválido. Use AAAA-MM-DD."
