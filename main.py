from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs
from langcodes import Language

def translates(query):
    det=detect(query)
    try:
        lang = Language.get(det).display_name()
    except:
        lang = det
    if det != 'en':
        translation = GoogleTranslator(source='auto', target='en').translate(query)
    else:
        translation = query
    
    low= translation.lower()
    if any(word in low for word in ['order', 'track', 'delivery', 'shipping', 'where']):
        response = "You can track your order using the tracking number sent to your email."
    elif any(word in low for word in ['return', 'refund', 'money back']):
        response = "Our return policy allows returns within 30 days with a full refund."
    elif any(word in low for word in ['cancel', 'change', 'modify']):
        response = "You can cancel or modify your order within 24 hours of purchase."
    elif any(word in low for word in ['help', 'support', 'contact', 'question']):
        response = "Our support team is here to help. Please describe your issue in detail."
    elif any(word in low for word in ['price', 'cost', 'how much']):
        response = "You can view pricing on our website or contact sales for a quote."
    else:
        response = "Thank you for contacting us. Our support team will assist you shortly."
    
    if det != 'en':
        og_response = GoogleTranslator(source='en', target=det).translate(response)
    else:
        og_response = response
    
    return {
        'detected': lang,
        'translation': translation,
        'response': response,
        'og_response': og_response
    }

def main():
    print("=== Multilingual Translator ===\n")
    print("Example: ¿Dónde está mi pedido? -> Where is my order?\n")
    
    while True:
        query = input("Enter query (or 'q' to quit): ").strip()
        
        if query.lower() == 'q':
            print("Goodbye!")
            break
        if not query:
            continue
        
        try:
            result = translates(query)
            print(f"\nDetected Language: {result['detected']}")
            print(f"English Translation: {result['translation']}")
            print(f"\nResponse (English):\n   {result['response']}")
            print(f"\nResponse ({result['detected']}):\n   {result['og_response']}\n")
            print("~" * 60 + "\n")
            
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
