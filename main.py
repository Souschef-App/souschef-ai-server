import logging

from app.server import Server

logging.basicConfig(level=logging.INFO)

def main():
    logger = logging.getLogger()
    logger.info("Running AI...")

    server = Server()
    server.listen()


if __name__ == "__main__":
    main()
