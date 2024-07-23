from flask import Blueprint, request, jsonify
from models import InventoryItem, db
from flask_jwt_extended import jwt_required

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/add', methods=['POST'])
@jwt_required()
def add_item():
    data = request.get_json()
    new_item = InventoryItem(name=data['name'], quantity=data['quantity'], barcode=data['barcode'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully'}), 201

@inventory_bp.route('/list', methods=['GET'])
@jwt_required()
def list_items():
    items = InventoryItem.query.all()
    result = [{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'barcode': item.barcode} for item in items]
    return jsonify(result)

@inventory_bp.route('/update/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    item = InventoryItem.query.get_or_404(item_id)
    item.name = data['name']
    item.quantity = data['quantity']
    item.barcode = data['barcode']
    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})

@inventory_bp.route('/delete/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})
