import streamlit as st

class StreamlitRouter:
    def __init__(self):
        self.routes = {}

    def register(self, func, path, methods=None):
        self.routes[path] = func

    def build(self, route_name, params=None):
        path = f"/{route_name}"
        if params:
            path += "?" + "&".join(f"{k}={v}" for k, v in params.items())
        return (path,)

    def redirect(self, path):
        st.experimental_set_query_params(path=path)

    def serve(self):
        query_params = st.experimental_get_query_params()
        path = query_params.get('path', ['/'])[0]
        func, params = self.match_route(path)
        if func:
            func(self, **params)

    def match_route(self, path):
        for route_path, func in self.routes.items():
            if route_path == path.split('?')[0]:
                query_string = path.split('?')[1] if '?' in path else ''
                params = {k: v for k, v in [p.split('=') for p in query_string.split('&') if '=' in p]}
                return func, params
        return None, {}

    def map(self, path):
        def decorator(func):
            self.register(func, path)
            return func
        return decorator

def index(router):
    st.text("Front page index")
    x = st.number_input("task id", min_value=0)
    if st.button("Create task"):
        router.redirect(*router.build("create_task", {"x": x}))
    if st.button("Cancel task"):
        router.redirect(*router.build("cancel_task", {"x": x}))
    if st.button("View task"):
        router.redirect(*router.build("view_task", {"x": x}))
    st.text("Others on page index")

def cancel_task(router, x):
    st.text(f"Front page cancel task x={x}")
    if st.button("Back to index"):
        router.redirect(*router.build("index"))
    st.text("Others on page cancel task")

def create_task(router, x):
    st.text(f"Front page create task x={x}")
    if st.button("Back to index"):
        router.redirect(*router.build("index"))
    st.text("Others on page create task")

router = StreamlitRouter()
router.register(index, '/')
router.register(cancel_task, "/tasks/<int:x>", methods=['DELETE'])
router.register(create_task, "/tasks/<int:x>", methods=['POST'])

@router.map("/tasks/view_task")
def view_task(router, x):
    st.text(f"Front page view task x={x}")
    if st.button("Back to index 2"):
        router.redirect(*router.build("index"))
    st.text("Others on page view task")

router.serve()
