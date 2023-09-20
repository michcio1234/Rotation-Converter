def calc_new_setting(
    old_gilza_weight,
    old_thickness,
    old_setting,
    old_weight,
    new_gilza_weight,
    new_thickness,
    new_weight,
):
    res = (old_setting * (new_weight - new_gilza_weight)) / (
        (old_weight - old_gilza_weight) * (new_thickness / old_thickness)
    )
    return round(res)


def _test():
    assert (
        calc_new_setting(
            old_gilza_weight=50,
            new_gilza_weight=60,
            old_thickness=10,
            new_thickness=30,
            old_weight=250,
            new_weight=300,
            old_setting=500,
        )
        == 200
    )

    assert (
        calc_new_setting(
            old_gilza_weight=50,
            new_gilza_weight=60,
            old_thickness=30,
            new_thickness=10,
            old_weight=250,
            new_weight=300,
            old_setting=500,
        )
        == 1800
    )


if __name__ == "__main__":
    _test()
