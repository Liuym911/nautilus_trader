# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

import asyncio

from nautilus_trader.adapters.tardis.factories import get_tardis_http_client
from nautilus_trader.adapters.tardis.factories import get_tardis_instrument_provider
from nautilus_trader.common.component import init_logging
from nautilus_trader.common.config import InstrumentProviderConfig
from nautilus_trader.common.enums import LogLevel
from nautilus_trader.core import nautilus_pyo3


async def run():
    nautilus_pyo3.init_tracing()
    init_logging(level_stdout=LogLevel.TRACE)

    _guard = init_logging()
    http_client = get_tardis_http_client()

    # Test loading all instrument for specified exchanges
    exchanges = ["deribit"]
    filters = {
        "venues": frozenset(exchanges),
        "quote_currency": frozenset(["BTC"]),
        # "base_currency": frozenset(["USDT"]),
        "instrument_type": frozenset(["option"]),
    }

    # config = InstrumentProviderConfig(load_all=True, filters=filters)
    # provider = get_tardis_instrument_provider(http_client, config)
    #
    # await provider.initialize()

    # Test loading only specified instruments
    # instrument_ids = [
    #     "XBT-USD.OKEX",
    #     "ETH-USD.OKEX",
    # ]

    # config = InstrumentProviderConfig(load_ids=frozenset(instrument_ids))
    config = InstrumentProviderConfig(load_all=True, filters=filters)
    provider = get_tardis_instrument_provider(http_client, config)

    await provider.initialize()


if __name__ == "__main__":
    asyncio.run(run())
