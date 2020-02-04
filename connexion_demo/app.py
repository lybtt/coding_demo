import connexion

if __name__ == '__main__':
    import sys
    if sys.platform == 'win32':
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = connexion.FlaskApp(__name__, server='tornado')
    app.add_api('api.yaml', arguments={'title': '我的api', 'version': 'v1.0'})
    app.run(port=8999)