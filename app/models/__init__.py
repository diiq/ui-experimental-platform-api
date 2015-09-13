from experiment import Experiment
from user import User
from participation import Participation
from session import Session

import inspect
import sys

all_models = [cls for _, cls in
              inspect.getmembers(sys.modules[__name__],
                                 inspect.isclass)]


# flake8: noqa
