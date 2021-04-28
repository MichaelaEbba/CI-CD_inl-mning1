import Calculator as c


class Test:
    def test_add(self):
        assert 5 == c.add(3, 2)
        assert 19 == c.add(8, 11)
