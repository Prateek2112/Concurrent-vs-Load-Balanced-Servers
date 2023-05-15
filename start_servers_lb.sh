

ports=(8000 8001 8002)

cleanup() {
    for i in "${ports[@]}"
    do
        kill -9 $(lsof -t -i:$i)
    done
}

trap cleanup EXIT
for i in "${ports[@]}"
do
    python3 server_lb.py $i &
done

python3 load_balancer.py