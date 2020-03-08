####################################################################################################################################
# Snake game agent navigation via the use of artificial intelligence
#
# Copyright (C) 2019 Project contributors
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation, either version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License along with this program. If not, see
# <http://www.gnu.org/licenses/>.


####################################################################################################################################
from game.interface import UserInterface
from game.snake import Definition as Game
from agent.human import Definition as Agent


####################################################################################################################################
# Define the default game
game = Game()
agent = Agent(game)
interface = UserInterface(game, agent)
interface.show()
