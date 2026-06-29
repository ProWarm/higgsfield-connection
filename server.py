import os
import uvicorn

# Пробуем разные пути импорта пакета
try:
    from higgsfield_unlimited_mcp.server import mcp
except ImportError:
    try:
        from higgsfield_unlimited_mcp import mcp
    except ImportError:
        raise RuntimeError(
            "Не удалось импортировать mcp из пакета. "
            "Проверь структуру higgsfield-unlimited-mcp."
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app = mcp.http_app()          # SSE endpoint → /sse
    uvicorn.run(app, host="0.0.0.0", port=port)
