#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                     108, 256, 512]), 1024)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)

    def test_positives_and_negatives_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6351, 9735, -8649, 4405, 6261, -1907, -9443, -6308,
                    7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                    -6683, 715, -8738, 9678, -1081, 4730, -1376, 9126,
                    -8394, 9732, 1695, -4932, -2100, -6920, 2219, -7319,
                    -1193, -422, 9312, 9508, -2690, -9206, 4461, 2997, -6753,
                    -7824, 3097, 1681, 3401, 7221, 1758, -1990, 4958, 4347,
                    7054, 545, 3492, -7285, -1672, 2230, -4576, -3121,
                    -6736, -537, 9823, 4281, -8003, 327, 1824, -1973, -9844,
                    29, 3596, 1108, 6702, 4873, -9452, -5949, -9640, -2156,
                    -4104, 5772, 5121, -2186, -4870, -4116, 6443, -9381,
                    -9388, 8552, 3582, 3500, 7924, 211, -2976, 6346, -5405,
                    899, -3432, -2550, -3353, 6944, 9623]), 9823)

    def test_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -562553, -3088955, -6711290, -4817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -8433749, -7251403, -5117635, -2979207, -1335257,
                    -6867266, -9073637, -6224732, -1080801, -1080228,
                    -6801278, -8351954, -1736432, -746131, -4376995,
                    -967891, -4663691, -71562, -7153670, -8038202,
                    -7893047, -9350883, -1132134, -3675971, -8495354,
                    -9158229, -9310087, -6319598, -8961209, -4906000,
                    -386471, -639929, -2676965, -6881679, -6258057,
                    -5490677, -1107298, -4199148, -5933601, -9917695,
                    -7759849, -7045734, -4885806, -9485075, -5119579,
                    -4147063, -7622811, -4671971, -5439539, -840414,
                    -3671742, -4400074, -3549343, -9146070, -6071672,
                    -7213213, -1307446, -3936098, -2415520, -9162654,
                    -6129976, -5791439, -3481890, -7828832, -6954726,
                    -5272933, -4952516, -6115545, -8333464, -7271456,
                    -4097027, -4342575, -8400559, -8235052, -4373818,
                    -8054214, -8565596, -639225, -2292452, -4269529,
                    -7202853, -6891036, -4379807, -7955196, -1536591,
                    -2839083, -2586661, -9941097, -3136620]), -71562)

    def test_ints_and_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)
        
    def test_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])









if __name__ == '__main__':
    unittest.main()