from typing import Dict

from honey_ryder.connectors.influxdb.influxdb_processor import InfluxDBProcessor


def test_process_event_packet(laps_dict: Dict, processor: InfluxDBProcessor):

    results = processor._process_laps(laps_dict, 'test_laps')
    assert len(results) == 480


def test_process_motion_packet(car_motion_dict: Dict, processor: InfluxDBProcessor):

    results = processor.extract_car_array_data(car_motion_dict, 'test_motion')
    assert len(results) == 375