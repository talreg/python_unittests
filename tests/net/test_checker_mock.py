import unittest,unittest.mock
from net.StatusCheck import StatusCheck
from net.Title import Title

class TestChecker(unittest.TestCase):
    """docstring for TestChecker"""

    # here is patching an object. every instance of this object will be patched (= it will return immediately and always the value we provided)
    # and we can also make sure that the containing object is calling it the right way
    @unittest.mock.patch.object(StatusCheck,'get_title')
    def test_mock_title_object(self,mock_gt):
        url="www.google.com"
        t=Title()
        mock_gt.return_value="test"
        value=t.get_url_title(url)
        # this is a nice feature, we can assure that this internal module was called with a certain parameter
        mock_gt.assert_called_with()
        # This is a great feature, where we replace the result of the inner module
        self.assertTrue(value=="test","should return mocked title ")
        # however, the other methods works without an issue, as usual.
        self.assertTrue(t.check_url(url)==200)
