import sys
import os
import unittest
sys.path.append(os.path.abspath('../app'))
import app.main as main

class TestMain(unittest.TestCase):
  def setUp(self):
    print('setup main')
    self.cargos = {
      'A': {'o_lat': 44.4582983, 'o_lng': -73.161604, 'd_lat': 42.3636331, 'd_lng': -87.8447938},
      'B': {'o_lat': 13.756331, 'o_lng': 100.501762, 'd_lat': 13.528650, 'd_lng': 99.813263},
      'C': {'o_lat': 39.9524, 'o_lng': -75.1636, 'd_lat': 43.1031, 'd_lng': -79.0303},
      'D': {'o_lat': 1, 'o_lng': 1, 'd_lat': 45, 'd_lng': 13}
    }
    self.trucks = {
      'Banana Boat': {'lat': 5, 'lng': 4},
      'Windfall': {'lat': -79.406307, 'lng': 0.314931},
      'Coffee Beans': {'lat': -6.86997, 'lng': -75.045851},
      'Batmobile': {'lat': 40.741895, 'lng': -73.989308},
      'Chariot': {'lat': 41.894802, 'lng': 30.485338},
      'Caramel Swirls': {'lat': 47.372394, 'lng': 8.542333},
      'Zebra Stripes': {'lat': -1.283253, 'lng': 36.817245},
      'Slam Dunk': {'lat': 35.682839, 'lng': 139.759455},
      'Alfredo': {'lat': 42.6011194, 'lng': -89.6384532}
    }

  def tearDown(self):
    print('teardown main')

  def test_shortest_distance(self):
    self.assertEqual(main.shortest_distance(self.cargos, self.trucks), {
      'A': {'Alfredo': 18.390497377276045},
      'B': {'Slam Dunk': 90.64425911395827},
      'C': {'Batmobile': 6.981600672073832},
      'D': {'Banana Boat': 46.0}
    })