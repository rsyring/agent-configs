To avoid problems with Freezegun's patching logic, always get `datetime` module objects
from the top-level module:

```
import datetime
# OR
import datetime as dt
```
