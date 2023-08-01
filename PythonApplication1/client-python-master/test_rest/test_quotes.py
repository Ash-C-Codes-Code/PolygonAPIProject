from base import BaseTest
from polygon.rest.models import (
    Quote,
    LastQuote,
    ForexQuote,
    LastForexQuote,
    RealTimeCurrencyConversion,
)


class QuotesTest(BaseTest):
    def test_list_quotes(self):
        quotes = [q for q in self.c.list_quotes("AAPL")]
        expected = [
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872800402200,
                sequence_number=19288684,
                sip_timestamp=1652191872800638700,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=15,
                bid_price=155.85,
                bid_size=5,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872774195000,
                sequence_number=19288618,
                sip_timestamp=1652191872774441200,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872773756000,
                sequence_number=19288617,
                sip_timestamp=1652191872773945300,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=12,
                bid_price=155.85,
                bid_size=3,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872753255000,
                sequence_number=19288557,
                sip_timestamp=1652191872753443000,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=3,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872751394300,
                sequence_number=19288549,
                sip_timestamp=1652191872751569400,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=21,
                bid_price=155.86,
                bid_size=1,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872750485800,
                sequence_number=19288528,
                sip_timestamp=1652191872750826800,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=11,
                bid_price=155.86,
                bid_size=1,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872750458400,
                sequence_number=19288525,
                sip_timestamp=1652191872750633000,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=21,
                bid_price=155.86,
                bid_size=2,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872750206000,
                sequence_number=19288519,
                sip_timestamp=1652191872750488300,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=1,
                bid_exchange=21,
                bid_price=155.86,
                bid_size=2,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872748910000,
                sequence_number=19288491,
                sip_timestamp=1652191872749094400,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=2,
                bid_exchange=21,
                bid_price=155.86,
                bid_size=2,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872690425000,
                sequence_number=19288166,
                sip_timestamp=1652191872690661000,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=2,
                bid_exchange=19,
                bid_price=155.86,
                bid_size=1,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872690177000,
                sequence_number=19288135,
                sip_timestamp=1652191872690386918,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=2,
                bid_exchange=15,
                bid_price=155.85,
                bid_size=5,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872688200000,
                sequence_number=19288101,
                sip_timestamp=1652191872688383612,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=15,
                bid_price=155.85,
                bid_size=5,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872687729447,
                sequence_number=19288096,
                sip_timestamp=1652191872687968794,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872686891199,
                sequence_number=19288093,
                sip_timestamp=1652191872687168881,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=15,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872677145000,
                sequence_number=19288051,
                sip_timestamp=1652191872677330035,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=4,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872676782000,
                sequence_number=19288049,
                sip_timestamp=1652191872676973864,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=4,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=3,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872664864000,
                sequence_number=19288026,
                sip_timestamp=1652191872665047506,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=4,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872663336000,
                sequence_number=19288010,
                sip_timestamp=1652191872663527001,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=3,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872663291000,
                sequence_number=19288009,
                sip_timestamp=1652191872663480163,
                tape=3,
                trf_timestamp=None,
            ),
            Quote(
                ask_exchange=19,
                ask_price=155.87,
                ask_size=2,
                bid_exchange=19,
                bid_price=155.85,
                bid_size=4,
                conditions=None,
                indicators=None,
                participant_timestamp=1652191872663233957,
                sequence_number=19288004,
                sip_timestamp=1652191872663407429,
                tape=3,
                trf_timestamp=None,
            ),
        ]
        self.assertEqual(quotes, expected)

    def test_get_last_quote(self):
        last = self.c.get_last_quote("AAPL")
        expected = LastQuote(
            ticker="AAPL",
            trf_timestamp=None,
            sequence_number=26006043,
            sip_timestamp=1652192754171838500,
            participant_timestamp=1652192754171619000,
            ask_price=155.66,
            ask_size=14,
            ask_exchange=11,
            conditions=None,
            indicators=None,
            bid_price=155.65,
            bid_size=1,
            bid_exchange=19,
            tape=3,
        )

        self.assertEqual(last, expected)

    def test_get_last_forex_quote(self):
        last_forex = self.c.get_last_forex_quote("AUD", "USD")
        expected = LastForexQuote(
            last=ForexQuote(
                ask=0.69527, bid=0.6952, exchange=48, timestamp=1652193694000
            ),
            symbol="AUD/USD",
        )

        self.assertEqual(last_forex, expected)

    def test_get_real_time_currency_conversion(self):
        conversion = self.c.get_real_time_currency_conversion("AUD", "USD", 100, 2)
        expected = RealTimeCurrencyConversion(
            converted=69.31,
            from_=None,
            initial_amount=100,
            last=ForexQuote(
                ask=1.4436264, bid=1.4427932, exchange=48, timestamp=1652195426000
            ),
            to="USD",
        )

        self.assertEqual(conversion, expected)
