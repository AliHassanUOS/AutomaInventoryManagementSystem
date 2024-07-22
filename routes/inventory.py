from flask import Blueprint, request, jsonify
from models import InventoryItem, db

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = InventoryItem(name=data['name'], quantity=data['quantity'], barcode=data['barcode'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully'}), 201

@inventory_bp.route('/list', methods=['GET'])
def list_items():
    items = InventoryItem.query.all()
    result = [{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'barcode': item.barcode} for item in items]
    return jsonify(result)
