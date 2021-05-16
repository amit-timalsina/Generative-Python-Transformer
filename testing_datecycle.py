import time
from datetime import datetime

end_time = time.time()
start_time = end_time - 86400


start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')

query = f"flask language:Python created:{start_time_str}..{end_time_str}"
print(query)