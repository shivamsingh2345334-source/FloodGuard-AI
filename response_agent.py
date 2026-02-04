if __name__ == "__main__":
    print(response_agent("High"))

def response_agent(risk_level):

    if risk_level == "High":
        return {
            "alert": "🚨 Immediate Evacuation Required",
            "resources": ["Rescue Boats", "Medical Teams", "Shelters"],
            "action": "Evacuate within 6 hours"
        }

    elif risk_level == "Medium":
        return {
            "alert": "⚠️ Flood Warning",
            "resources": ["Ambulances", "Rescue Teams"],
            "action": "Prepare evacuation + monitor situation"
        }

    else:
        return {
            "alert": "✅ Normal Conditions",
            "resources": ["Monitoring Teams"],
            "action": "Continue surveillance"
        }
