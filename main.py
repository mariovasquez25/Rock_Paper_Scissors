from RPS_utils import fitting_and_training
from players import player, leonardo, raphael, donatello, michelangelo
from play import play
import warnings
warnings.filterwarnings('ignore')

mlp = fitting_and_training(500)

play(player, leonardo, 1000, model=mlp)
play(player, raphael, 1000, model=mlp)
play(player, donatello, 1000, model=mlp)
play(player, michelangelo, 1000, model=mlp)
