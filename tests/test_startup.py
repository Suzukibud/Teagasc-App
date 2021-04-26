from django.urls import reverse
from pytest import fail


def test_web(client):
    url = reverse("importExport")
    response = client.get(url)
    assert response.status_code == 302


def test_grass_stock_rate_1():
    dairy_cow_nitrates = 89 * 10
    cattle_1_nitrates = 65 * 15
    cattle_2_nitrates = 57 * 4

    total_nitrates = dairy_cow_nitrates + cattle_1_nitrates + cattle_2_nitrates
    total_nitrates /= 20
    total_nitrates = round(total_nitrates, 2)

    assert total_nitrates == 104.65

def test_grass_stock_rate_2():
    dairy_cow_nitrates = 89 * 30
    cattle_1_nitrates = 65 * 55
    cattle_2_nitrates = 57 * 40

    total_nitrates = dairy_cow_nitrates + cattle_1_nitrates + cattle_2_nitrates
    total_nitrates /= 20
    total_nitrates = round(total_nitrates, 2)

    assert total_nitrates == 426.25

def test_wholefarm_stocking_rate_1():
    dairy_cow_nitrates = 10 * 89
    cattle_1_nitrates = 15 * 65
    cattle_2_nitrates = 4 * 57

    total_nitrates = dairy_cow_nitrates + cattle_1_nitrates + cattle_2_nitrates
    total_nitrates /= 23
    wfsr = round(total_nitrates, 2)

    assert wfsr == 91

def test_wholefarm_stocking_rate_2():
    dairy_cow_nitrates = 50 * 89
    cattle_1_nitrates = 35 * 65
    cattle_2_nitrates = 24 * 57

    total_nitrates = dairy_cow_nitrates + cattle_1_nitrates + cattle_2_nitrates
    total_nitrates /= 43
    wfsr = round(total_nitrates, 2)

    assert wfsr == 188.21

def test_livestock_unit_hectacre_1():
    dairy_lsu = 10 * 1
    cattle_1_lsu = 15 * 1
    cattle_2_lsu = 4 * 0.4

    total_lsu = dairy_lsu + cattle_1_lsu + cattle_2_lsu
    total_lsu /= 23
    total_lsu = round(total_lsu,2)

    assert total_lsu == 1.16

def test_livestock_unit_hectacre_2():
    dairy_lsu = 30 * 1
    cattle_1_lsu = 25 * 1
    cattle_2_lsu = 14 * 0.4

    total_lsu = dairy_lsu + cattle_1_lsu + cattle_2_lsu
    total_lsu /= 23
    total_lsu = round(total_lsu,2)

    assert total_lsu == 2.63
    
def test_record5_1():
    hectacres = 10
    time_r = 6
    nitrates = 2093
    land = 20

    time_r /= 12
    time_r = round(time_r,2)
    hectacres *= time_r
    hectacres = round(hectacres,2)

    gsr = nitrates / land
    gsr = round(gsr,2)
    assert gsr == 104.65

    hectacres += land
    gsr = nitrates / hectacres
    gsr = round(gsr,2)
    assert gsr == 83.72

def test_record5_2():
    hectacres = 8
    time_r = 4
    nitrates = 2093
    land = 30

    time_r /= 12
    time_r = round(time_r,2)
    hectacres *= time_r
    hectacres = round(hectacres,2)

    gsr = nitrates / land
    gsr = round(gsr,2)
    assert gsr == 69.77

    hectacres += land
    gsr = nitrates / hectacres
    gsr = round(gsr,2)
    assert gsr == 64.12

def test_import_slurry_nitrates_1():
    total_nitrates = 2093
    import_ = 10
    land = 23
    nitrate_import = import_ * 5

    total_nitrates += nitrate_import
    wfsr = total_nitrates / land
    wfsr = round(wfsr,2)

    assert wfsr == 93.17

def test_import_slurry_nitrates_2():
    total_nitrates = 2093
    import_ = 20
    land = 43
    nitrate_import = import_ * 5

    total_nitrates += nitrate_import
    wfsr = total_nitrates / land
    wfsr = round(wfsr,2)

    assert wfsr == 51.0

def test_import_manure_nitrates_1():
    total_nitrates = 2093
    import_ = 10
    land = 23
    nitrate_import = import_ * 4.5

    total_nitrates += nitrate_import
    wfsr = total_nitrates / land
    wfsr = round(wfsr,2)

    assert wfsr == 92.96

def test_import_manure_nitrates_2():
    total_nitrates = 2093
    import_ = 20
    land = 50
    nitrate_import = import_ * 4.5

    total_nitrates += nitrate_import
    wfsr = total_nitrates / land
    wfsr = round(wfsr,2)

    assert wfsr == 43.66

def test_slurry_export_nitrates_1():
    total_nitrates = 2093
    export = 10 * 5
    total_nitrates -= export

    wfsr = total_nitrates /23
    wfsr = round(wfsr,2)

    assert wfsr == 88.83

def test_slurry_export_nitrates_2():
    total_nitrates = 2093
    export = 30 * 5
    total_nitrates -= export

    wfsr = total_nitrates /23
    wfsr = round(wfsr,2)

    assert wfsr == 84.48

def test_manure_export_nitrates_1():
    total_nitrates = 2093
    export = 30 * 5
    total_nitrates -= export

    wfsr = total_nitrates /23
    wfsr = round(wfsr,2)

    assert wfsr == 84.48

def test_manure_export_nitrates_2():
    total_nitrates = 2093
    export = 30 * 5
    total_nitrates -= export

    wfsr = total_nitrates /23
    wfsr = round(wfsr,2)

    assert wfsr == 84.48

