import pytest
from app import db
from app.subscribe.store_subscription_data import store_subscription_data
from app.subscribe.store_subscription_data import store_subscription_data


def test_store_subscription_invalid_data(db_session):
    # Setup invalid test subscription data
    subscription_data = {
        'user_id': 1,
        'subscription_type': 'unknown_type',
        'start_date': 'invalid_date',
        'end_date': '2022-12-31'
    }
    
    # Call the function to test and assert it raises an error
    with pytest.raises(ValueError):
        store_subscription_data(subscription_data)

def test_store_subscription_existing_user(db_session):
    # Setup test subscription data for a user who already has a subscription
    subscription_data = {
        'user_id': 2,
        'subscription_type': 'premium',
        'start_date': '2022-01-01',
        'end_date': '2022-12-31'
    }
    
    # Call the function to test
    result = store_subscription(subscription_data)
    
    # Assert the result
    assert result is False
    # Optionally check that the existing subscription hasn't been modified
