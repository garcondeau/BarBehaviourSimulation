GREEN='\033[1;32m'
NC='\033[0m'

echo ""
echo -e "${GREEN}================================================"
echo -e "================ REBUILD STARTED ==============="
echo -e "================================================${NC}"
echo ""

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

docker-compose -f docker-compose.yaml up --build -d

watchman-make -p '**/*.py' -s 1 --run 'touch uwsgi-reload'