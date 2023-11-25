import random

from .meters.main import meter_type
from .meters.residential import residential
from .meters.industry import industry
from .meters.feed_in import feed_in
from .meters.residential_feed_in import residential_feed_in
from .constants import METER_OCCURENCES

def main(seed):
    random.seed(seed)
    meter = random.choices(list(meter_type), METER_OCCURENCES, k=1)[0]
    match meter:
        case meter_type.residential:
            meter = residential(seed)
        case meter_type.industry:
            meter = industry(seed)
        case meter_type.feed_in:
            meter = feed_in(seed)
        case meter_type.residential_feed_in:
            meter = residential_feed_in(seed)
    print(meter.string())