import logging
import json
import requests

from flask import jsonify, Blueprint, abort
from components.riot import Riot


LOG = logging.getLogger(__name__)
CURRENT_REGION = 'euw1'
CDRAGON_ASSET_URL = 'https://raw.communitydragon.org/pbe/game/data/items/icons2d/'

blueprint = Blueprint('views', __name__)
# rest_api.add_resource(kanban_card.KanbanListView, '/api/admin/reference', methods=['POST', 'PUT', 'PATCH'])
# rest_api.add_resource(kanban_card.KanbanView, '/api/admin/reference/<reference>', methods=['GET', 'DELETE'])


@blueprint.route('/status/is_up', methods=['GET'])
def is_up():
    return jsonify(is_up=True)


@blueprint.route('/riot/summoners/<name>', methods=['GET'])
def summoner(name):
    rito = Riot()
    return jsonify(summoner=rito.summoner.by_name('euw1', name))


@blueprint.route('/riot/items', methods=['GET'])
def items():
    rito = Riot()
    riot_data = rito.data_dragon.versions_for_region(CURRENT_REGION)
    LOG.info(riot_data)
    items = rito.data_dragon.items(version=riot_data['n']['item'])
    for item_name, obj in items['data'].items():
        obj['image_url'] = Riot.get_image_url(riot_data, obj)
    LOG.info(items)
    return jsonify(items=items)


@blueprint.route('/cdragon/items', methods=['GET'])
def cdragon_items():
    resp = requests.get('https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/items.json')
    if not resp.status_code == 200:
        abort(404)
    raw_items = resp.json()
    items = []
    for item in raw_items:
        # active item ?
        if not item['inStore']:
            continue
        LOG.info(item['inStore'])
        # is in Summoner Rift map ?
        if 'SR' not in item['mapStringIdInclusions']:
            continue

        icon_uri = item['iconPath'].split('/')[-1].lower()
        item['image_url'] = CDRAGON_ASSET_URL + icon_uri
        items.append(item)
    return jsonify(items=items)


@blueprint.route('/riot/cdn', methods=['GET'])
def cdn():
    rito = Riot()
    riot_data = rito.data_dragon.versions_for_region(CURRENT_REGION)
    return jsonify(cdn=rito.data_dragon.items(version=riot_data['cdn']))


@blueprint.route('/riot/champions', methods=['GET'])
def champions():
    rito = Riot()
    riot_data = rito.data_dragon.versions_for_region(CURRENT_REGION)
    champions = rito.data_dragon.champions(version=riot_data['n']['champion']).get('data')
    for champ_name, obj in champions.items():
        obj['image_url'] = Riot.get_image_url(riot_data, obj)
    return jsonify(champions=champions)
