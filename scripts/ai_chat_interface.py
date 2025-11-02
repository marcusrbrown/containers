"""
AI Chat Interface for Container Templates

This module provides a natural language interface for:
- Template discovery through conversation
- Parameter configuration via chat
- Code analysis and optimization suggestions
- Interactive template customization
"""

import json
import logging
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

import yaml

from .ai_core import get_ai_core
from .template_intelligence import TemplateIntelligence

logger = logging.getLogger(__name__)


@dataclass
class ChatSession:
    """Represents a chat session with context"""

    session_id: str
    messages: List[Dict[str, str]]
    context: Dict[str, Any]
    current_project: Optional[str] = None
    current_template: Optional[str] = None
    suggested_parameters: Optional[Dict[str, Any]] = None


class TemplateAssistant:
    """AI-powered assistant for template management"""

    def __init__(self):
        self.ai_core = get_ai_core()
        self.template_intelligence = TemplateIntelligence()
        self.sessions: Dict[str, ChatSession] = {}

        # System prompt for the assistant
        self.system_prompt = """
You are an expert DevOps assistant specializing in container templates and application architecture.

Your capabilities include:
1. Analyzing project requirements and recommending optimal container templates
2. Inferring configuration parameters from project descriptions
3. Providing code analysis and optimization suggestions
4. Helping users customize templates for their specific needs
5. Explaining containerization best practices

Guidelines:
- Ask clarifying questions when requirements are unclear
- Provide specific, actionable recommendations
- Explain your reasoning for template choices
- Suggest parameter values with explanations
- Always consider security, performance, and maintainability
- Be concise but thorough in explanations

Available template categories:
- Node.js applications (Express, React, Vue, Next.js)
- Python applications (FastAPI, Django, Flask, Data Science)
- Go microservices
- Rust applications
- Database containers (PostgreSQL, Redis, MongoDB)
- Infrastructure (Nginx, monitoring, logging)

When recommending templates, always include:
1. Template name and rationale
2. Confidence score (0-100)
3. Suggested parameters
4. Alternative options
5. Next steps for implementation
"""

    def start_session(self, session_id: Optional[str] = None) -> str:
        """Start a new chat session"""
        if session_id is None:
            import uuid

            session_id = str(uuid.uuid4())

        self.sessions[session_id] = ChatSession(
            session_id=session_id, messages=[], context={}, suggested_parameters={}
        )

        return session_id

    def chat(self, session_id: str, user_message: str) -> str:
        """Process user message and return assistant response"""
        if session_id not in self.sessions:
            session_id = self.start_session(session_id)

        session = self.sessions[session_id]

        # Add user message to session
        session.messages.append({"role": "user", "content": user_message})

        # Detect if this is a template request
        intent = self._detect_intent(user_message)

        # Handle different types of requests
        if intent == "analyze_project":
            response = self._handle_project_analysis(session, user_message)
        elif intent == "recommend_template":
            response = self._handle_template_recommendation(session, user_message)
        elif intent == "configure_parameters":
            response = self._handle_parameter_configuration(session, user_message)
        elif intent == "code_analysis":
            response = self._handle_code_analysis(session, user_message)
        elif intent == "general_question":
            response = self._handle_general_question(session, user_message)
        else:
            response = self._handle_conversation(session, user_message)

        # Add assistant response to session
        session.messages.append({"role": "assistant", "content": response})

        # Maintain conversation length limit
        max_length = 20
        if len(session.messages) > max_length:
            session.messages = session.messages[-max_length:]

        return response

    def _detect_intent(self, message: str) -> str:
        """Detect user intent from message"""
        message_lower = message.lower()

        # Project analysis keywords
        if any(
            word in message_lower for word in ["analyze", "scan", "examine", "project"]
        ):
            return "analyze_project"

        # Template recommendation keywords
        if any(
            word in message_lower
            for word in ["recommend", "suggest", "template", "need", "want"]
        ):
            return "recommend_template"

        # Parameter configuration keywords
        if any(
            word in message_lower
            for word in ["configure", "parameters", "settings", "config"]
        ):
            return "configure_parameters"

        # Code analysis keywords
        if any(
            word in message_lower
            for word in ["review", "optimize", "security", "performance"]
        ):
            return "code_analysis"

        # General questions
        if any(
            word in message_lower for word in ["what", "how", "why", "explain", "help"]
        ):
            return "general_question"

        return "conversation"

    def _handle_project_analysis(self, session: ChatSession, message: str) -> str:
        """Handle project analysis requests"""
        # Try to extract project path from message
        project_path = self._extract_project_path(message)

        if not project_path:
            return """I'd be happy to analyze your project! Please provide the path to your project directory, or you can describe your project and I'll help you choose the right template.

For example:
- "Analyze /path/to/my/project"
- "I have a Node.js Express API with PostgreSQL"
- "I'm building a Python FastAPI microservice"

What project would you like me to analyze?"""

        try:
            # Analyze the project
            analysis = self.template_intelligence.analyze_project(project_path)
            session.context["project_analysis"] = asdict(analysis)
            session.current_project = project_path

            # Format analysis results
            response = f"""## Project Analysis Results

**Project Type:** {analysis.project_type}
**Languages:** {', '.join(analysis.languages) if analysis.languages else 'None detected'}
**Frameworks:** {', '.join(analysis.frameworks) if analysis.frameworks else 'None detected'}
**Package Managers:** {', '.join(analysis.package_managers) if analysis.package_managers else 'None detected'}
**Complexity Score:** {analysis.complexity_score:.2f}/1.0

**Architecture Hints:**
{chr(10).join(f'- {hint}' for hint in analysis.architecture_hints)}

"""

            # Add recommendations if available
            if analysis.recommended_templates:
                response += "## Recommended Templates\\n\\n"
                for i, rec in enumerate(analysis.recommended_templates[:3], 1):
                    response += f"""**{i}. {rec.template_name}** (Confidence: {rec.confidence:.0%})
{rec.reasoning}

*Suggested parameters:* {', '.join(f'{k}={v}' for k, v in rec.parameters.items())}

"""

            response += "\\nWould you like me to help you configure any of these templates or analyze specific aspects of your project?"

            return response

        except Exception as e:
            logger.error(f"Project analysis failed: {e}")
            return f"I encountered an error analyzing the project at '{project_path}'. Please check that the path exists and is accessible. Error: {str(e)}"

    def _handle_template_recommendation(
        self, session: ChatSession, message: str
    ) -> str:
        """Handle template recommendation requests"""
        # Check if we have project context
        if session.current_project:
            try:
                recommendations = self.template_intelligence.recommend_templates(
                    session.current_project
                )
                return self._format_recommendations(recommendations)
            except Exception as e:
                logger.error(f"Template recommendation failed: {e}")

        # Use AI to understand requirements from natural language
        return self._get_ai_recommendations_from_description(session, message)

    def _handle_parameter_configuration(
        self, session: ChatSession, message: str
    ) -> str:
        """Handle parameter configuration requests"""
        if not session.current_template:
            return "Please first select a template that you'd like to configure. You can ask me to recommend templates or specify one directly."

        # Use AI to suggest parameters based on conversation
        prompt = f"""
Based on this conversation and the selected template '{session.current_template}', suggest optimal parameter configurations.

Conversation context: {json.dumps(session.context, indent=2)}
Latest message: {message}

Provide specific parameter values with explanations for why each value is recommended.
"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt},
        ]

        response = self.ai_core.chat_completion(messages)
        if response:
            return response.content
        else:
            return "I'm having trouble generating parameter suggestions right now. Could you be more specific about what you'd like to configure?"

    def _handle_code_analysis(self, session: ChatSession, message: str) -> str:
        """Handle code analysis and optimization requests"""
        # Try to extract code from message or context
        code = self._extract_code_from_message(message)

        if not code:
            return """I'd be happy to analyze your code! Please share the code you'd like me to review, or provide a file path. I can help with:

- Security vulnerability detection
- Performance optimization suggestions
- Best practice recommendations
- Code quality improvements

You can paste code directly or provide a file path like "analyze src/app.js" """

        # Use AI to analyze the code
        try:
            analysis_response = self.ai_core.analyze_code(code)
            if analysis_response:
                return f"""## Code Analysis Results

{analysis_response.content}

Would you like me to provide more specific suggestions for any of these areas?"""
            else:
                return "I'm having trouble analyzing the code right now. Please try again or check if the code is valid."

        except Exception as e:
            logger.error(f"Code analysis failed: {e}")
            return f"I encountered an error analyzing the code: {str(e)}"

    def _handle_general_question(self, session: ChatSession, message: str) -> str:
        """Handle general questions about containers and templates"""
        # Add context about available templates and capabilities
        context_prompt = f"""
Answer this question about container templates and DevOps practices: {message}

Available template categories in our system:
- Node.js applications (Express, React, Vue, Next.js)
- Python applications (FastAPI, Django, Flask, Data Science)
- Go microservices
- Rust applications
- Database containers (PostgreSQL, Redis, MongoDB)
- Infrastructure (Nginx, monitoring, logging)

Current conversation context: {json.dumps(session.context, indent=2) if session.context else 'None'}

Provide helpful, accurate information with practical examples when possible.
"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": context_prompt},
        ]

        response = self.ai_core.chat_completion(messages)
        if response:
            return response.content
        else:
            return "I'm having trouble processing your question right now. Could you rephrase it or be more specific?"

    def _handle_conversation(self, session: ChatSession, message: str) -> str:
        """Handle general conversation with context"""
        # Build conversation context
        conversation_messages = [{"role": "system", "content": self.system_prompt}]

        # Add relevant context
        if session.context:
            context_message = (
                f"Conversation context: {json.dumps(session.context, indent=2)}"
            )
            conversation_messages.append({"role": "system", "content": context_message})

        # Add recent messages
        conversation_messages.extend(session.messages[-10:])  # Last 10 messages

        response = self.ai_core.chat_completion(conversation_messages)
        if response:
            return response.content
        else:
            return "I'm having trouble understanding. Could you please rephrase your request or ask about a specific template or containerization topic?"

    def _extract_project_path(self, message: str) -> Optional[str]:
        """Extract project path from user message"""
        import re

        # Look for path patterns
        path_patterns = [
            r"analyze\s+([^\s]+)",
            r"project\s+(?:at\s+)?([^\s]+)",
            r"path[:\s]+([^\s]+)",
            r"(/[^\s]+)",  # Unix paths
            r"([A-Za-z]:[^\s]+)",  # Windows paths
        ]

        for pattern in path_patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                path = match.group(1)
                # Validate that it looks like a path
                if "/" in path or "\\\\" in path:
                    return path

        return None

    def _extract_code_from_message(self, message: str) -> Optional[str]:
        """Extract code from user message"""
        import re

        # Look for code blocks
        code_block_pattern = r"```(?:\\w+)?\\n(.*?)\\n```"
        match = re.search(code_block_pattern, message, re.DOTALL)
        if match:
            return match.group(1)

        # Look for inline code
        inline_code_pattern = r"`([^`]+)`"
        match = re.search(inline_code_pattern, message)
        if match:
            return match.group(1)

        # If message is mostly code (simple heuristic)
        if message.count("\\n") > 3 and any(
            keyword in message.lower()
            for keyword in ["function", "class", "def", "const", "var", "let"]
        ):
            return message

        return None

    def _get_ai_recommendations_from_description(
        self, session: ChatSession, message: str
    ) -> str:
        """Get template recommendations from natural language description"""
        prompt = f"""
Based on this project description, recommend the most suitable container templates:

Description: {message}

Available templates:
- nodejs-express: Express.js REST API applications
- nodejs-react: React frontend applications
- python-fastapi: FastAPI microservices
- python-django: Django web applications
- python-flask: Flask web applications
- python-data-science: Jupyter/pandas data analysis
- go-microservice: Go microservices
- rust-service: Rust applications
- postgresql: PostgreSQL database
- redis: Redis cache/database
- nginx: Web server/reverse proxy

For each recommendation, provide:
1. Template name and confidence score (0-100)
2. Why it's suitable for this project
3. Suggested configuration parameters
4. Any additional templates that might be useful

Format as a clear, structured response.
"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt},
        ]

        response = self.ai_core.chat_completion(messages)
        if response:
            return response.content
        else:
            return "I'm having trouble generating recommendations. Could you provide more details about your project requirements?"

    def _format_recommendations(self, recommendations: List) -> str:
        """Format template recommendations for display"""
        if not recommendations:
            return "I couldn't find any suitable template recommendations. Could you provide more details about your project?"

        response = "## Template Recommendations\\n\\n"

        for i, rec in enumerate(recommendations[:5], 1):
            response += f"""**{i}. {rec.template_name}** (Confidence: {rec.confidence:.0%})

{rec.reasoning}

*Suggested parameters:*
{chr(10).join(f'- {k}: {v}' for k, v in rec.parameters.items())}

*Alternatives:* {', '.join(rec.alternatives) if rec.alternatives else 'None'}

---

"""

        response += "\\nWould you like me to help you configure any of these templates or provide more details about a specific option?"

        return response

    def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Get summary of chat session"""
        if session_id not in self.sessions:
            return {"error": "Session not found"}

        session = self.sessions[session_id]

        return {
            "session_id": session_id,
            "message_count": len(session.messages),
            "current_project": session.current_project,
            "current_template": session.current_template,
            "context_keys": list(session.context.keys()),
            "has_analysis": "project_analysis" in session.context,
        }

    def export_session(self, session_id: str, format: str = "json") -> str:
        """Export chat session data"""
        if session_id not in self.sessions:
            return ""

        session = self.sessions[session_id]
        data = asdict(session)

        if format == "json":
            return json.dumps(data, indent=2, default=str)
        elif format == "yaml":
            return yaml.dump(data, default_flow_style=False)
        else:
            return str(data)


class InteractiveCLI:
    """Command-line interface for the template assistant"""

    def __init__(self):
        self.assistant = TemplateAssistant()
        self.session_id = None

    def start(self):
        """Start interactive chat session"""
        print("🤖 Container Template Assistant")
        print("=" * 40)
        print(
            "I'm here to help you find and configure the perfect container templates!"
        )
        print("Type 'help' for available commands, or 'quit' to exit.\\n")

        self.session_id = self.assistant.start_session()

        while True:
            try:
                user_input = input("You: ").strip()

                if user_input.lower() in ["quit", "exit", "bye"]:
                    print("\\n👋 Thanks for using Container Template Assistant!")
                    break

                if user_input.lower() == "help":
                    self._show_help()
                    continue

                if user_input.lower() == "summary":
                    self._show_session_summary()
                    continue

                if user_input.lower().startswith("export"):
                    self._export_session(user_input)
                    continue

                if not user_input:
                    continue

                # Get AI response
                print("\\n🤖 Assistant: ", end="")
                response = self.assistant.chat(self.session_id, user_input)
                print(response)
                print()

            except KeyboardInterrupt:
                print("\\n\\n👋 Thanks for using Container Template Assistant!")
                break
            except Exception as e:
                print(f"\\n❌ Error: {e}")
                print("Please try again or type 'help' for assistance.\\n")

    def _show_help(self):
        """Show help information"""
        help_text = """
📚 Available Commands:
- help: Show this help message
- quit/exit: Exit the assistant
- summary: Show session summary
- export [json|yaml]: Export session data

🎯 What I can help you with:
- Analyze your project: "Analyze /path/to/my/project"
- Get recommendations: "I need a template for a Node.js API"
- Configure parameters: "How should I configure the Express template?"
- Review code: "Can you analyze this code for security issues?"
- General questions: "What's the difference between Alpine and Ubuntu base images?"

💡 Example conversations:
- "I'm building a REST API with Python and PostgreSQL"
- "Analyze my project at ./my-app"
- "What template should I use for a React frontend?"
- "How do I optimize my Dockerfile for production?"
"""
        print(help_text)

    def _show_session_summary(self):
        """Show session summary"""
        summary = self.assistant.get_session_summary(self.session_id)
        print("\\n📊 Session Summary:")
        print(f"- Messages: {summary.get('message_count', 0)}")
        print(f"- Current project: {summary.get('current_project', 'None')}")
        print(f"- Current template: {summary.get('current_template', 'None')}")
        print(f"- Has analysis: {summary.get('has_analysis', False)}")
        print()

    def _export_session(self, command: str):
        """Export session data"""
        parts = command.split()
        format_type = parts[1] if len(parts) > 1 else "json"

        data = self.assistant.export_session(self.session_id, format_type)
        filename = f"chat_session_{self.session_id[:8]}.{format_type}"

        with open(filename, "w") as f:
            f.write(data)

        print(f"\\n💾 Session exported to {filename}")


def main():
    """Main CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="AI-powered container template assistant"
    )
    parser.add_argument("--session-id", help="Resume existing session")
    parser.add_argument("--message", help="Send single message (non-interactive)")
    parser.add_argument("--output", help="Output file for response")

    args = parser.parse_args()

    if args.message:
        # Non-interactive mode
        assistant = TemplateAssistant()
        session_id = assistant.start_session(args.session_id)
        response = assistant.chat(session_id, args.message)

        if args.output:
            with open(args.output, "w") as f:
                f.write(response)
            print(f"Response saved to {args.output}")
        else:
            print(response)
    else:
        # Interactive mode
        cli = InteractiveCLI()
        cli.start()


if __name__ == "__main__":
    main()
