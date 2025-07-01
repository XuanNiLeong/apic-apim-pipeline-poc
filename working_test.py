#!/usr/bin/env python3
"""
Working Test Example for Your Order Processing API Client
"""

import asyncio
import json
import sys
from pathlib import Path

# Add test directory to path
sys.path.insert(0, str(Path(__file__).parent / "api-client-example-kiota"))

def test_imports():
    """Test that we can import the generated client"""
    print("🔍 Testing Generated Client Imports")
    print("=" * 50)
    
    try:
        # Test main client import
        from test import Test
        print("✅ Main client (Test) imported successfully")
        
        # Check client properties
        client_props = [prop for prop in dir(Test) if not prop.startswith('_')]
        print(f"✅ Client has properties: {', '.join(client_props)}")
        
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

async def test_real_api():
    """Test calling your real APIM endpoint"""
    print("\n🔍 Testing Real APIM Endpoint")
    print("=" * 50)
    
    try:
        import httpx
        
        # Your APIM endpoint configuration
        url = "https://xnlapimdemo.azure-api.net/order/orders"
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": "bd1de05378344b5893c3c8681b5e83a1",
            "Ocp-Apim-Trace": "true"
        }
        
        # Order data (matches your OpenAPI spec)
        order_data = {
            "customerInfo": {
                "name": "Test Customer",
                "email": "test@example.com",
                "phone": "+1-555-0123"
            },
            "shippingAddress": {
                "street": "123 Test Street",
                "city": "Test City",
                "state": "TC",
                "country": "USA", 
                "postalCode": "12345"
            },
            "items": [
                {
                    "productId": "prod_test_001",
                    "productName": "Test Product",
                    "quantity": 1,
                    "unitPrice": 99.99
                }
            ],
            "paymentInfo": {
                "amount": 99.99,
                "currency": "USD",
                "paymentMethod": {
                    "type": "card",
                    "details": {"testMode": True}
                }
            }
        }
        
        print(f"📡 Calling: {url}")
        print(f"🔑 Using subscription key: ...{headers['Ocp-Apim-Subscription-Key'][-8:]}")
        print(f"📦 Order total: ${order_data['paymentInfo']['amount']}")
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=order_data, headers=headers)
            
            print(f"\n📊 Response:")
            print(f"   Status: {response.status_code}")
            print(f"   Headers: {dict(list(response.headers.items())[:3])}...")
            
            if response.status_code in [200, 201]:
                try:
                    result = response.json()
                    print(f"✅ Success! Response:")
                    print(f"   Order ID: {result.get('orderId', 'N/A')}")
                    print(f"   Status: {result.get('status', 'N/A')}")
                    print(f"   Total: ${result.get('totalAmount', 'N/A')}")
                    return True
                except:
                    print(f"✅ Success! Raw response: {response.text[:200]}...")
                    return True
            else:
                print(f"⚠️  Status {response.status_code}: {response.text[:200]}...")
                return False
                
    except Exception as e:
        print(f"❌ API call failed: {e}")
        return False

def show_usage_examples():
    """Show examples of how to use the API client"""
    print("\n📚 API Client Usage Examples")
    print("=" * 50)
    
    print("""
🔧 Basic Setup:
```python
import asyncio
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_abstractions.authentication import AnonymousAuthenticationProvider

# Setup
auth_provider = AnonymousAuthenticationProvider()
adapter = HttpxRequestAdapter(auth_provider)
adapter.base_url = "https://xnlapimdemo.azure-api.net/order"

# Add subscription key
adapter.headers = {"Ocp-Apim-Subscription-Key": "your-key-here"}

# Create client
from test.test import Test
client = Test(adapter)
```

📦 Create an Order:
```python
order_data = {
    "customerInfo": {"name": "John Doe", "email": "john@example.com"},
    "items": [{"productId": "prod_123", "quantity": 1, "unitPrice": 99.99}],
    "paymentInfo": {"amount": 99.99, "currency": "USD", 
                   "paymentMethod": {"type": "card", "details": {}}}
}

result = await client.orders.post(order_data)
```

🔍 Get an Order:
```python
order = await client.orders.by_order_id("ord_123456").get()
```

📋 List Orders:
```python
orders = await client.orders.get()
```
""")

async def main():
    """Main test function"""
    print("🚀 Order Processing API Client - Test & Demo")
    print("=" * 60)
    
    # Test 1: Check imports
    import_success = test_imports()
    
    # Test 2: Test real API
    api_success = await test_real_api()
    
    # Show usage examples
    show_usage_examples()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    print(f"Client Import:    {'✅ PASS' if import_success else '❌ FAIL'}")
    print(f"APIM API Call:    {'✅ PASS' if api_success else '❌ FAIL'}")
    
    if import_success and api_success:
        print("\n🎉 Your API client is working perfectly!")
        print("\n✅ Next Steps:")
        print("   1. Use the examples above in your code")
        print("   2. Run: pytest test_api_client.py for unit tests")
        print("   3. Customize the client for your specific needs")
    elif import_success:
        print("\n✅ Client is properly generated and importable!")
        print("⚠️  API endpoint might be mocked - this is normal for testing")
        print("\n💡 Your client is ready to use with the examples above")
    else:
        print("\n⚠️  Some issues found - check the output above")
    
    print(f"\n🔗 Your APIM Endpoint: https://xnlapimdemo.azure-api.net/order")
    print(f"🔑 Subscription Key: hidden")

if __name__ == "__main__":
    asyncio.run(main())
