

import redis
POOL=redis.ConnectionPool(max_connections=3,host='127.0.0.1', port=6379)