def get_minutes(seconds):
    """Convert seconds to minutes"""
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    if remaining_seconds:
        return f"{int(minutes)} minute{'s' if minutes > 1 else ''} et {int(remaining_seconds)} seconde{'s' if remaining_seconds > 1 else ''}"
    else:
        return f"{int(minutes)} minute{'s' if minutes > 1 else ''}"
