import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import (select_account, select_account,
                                      select_project, select_study)

# get api_client from pollination
api_client = get_api_client()

account = select_account('select-account', api_client)

if account:
    # if it is an organization it uses account_name otherwise username
    project_owner = account.get('username') or account.get('account_name')
    st.subheader(f'Hi {project_owner}! Select a project:')

    pcol1, pcol2 = st.columns(2)

    with pcol1:
        project = select_project(
            'select-project',
            api_client,
            project_owner=project_owner
        )
    with pcol2:
        st.json(project or '{}', expanded=False)

    if project:
        # get project name
        project_name = project.get('name')
        st.subheader('Select a study:')

        scol1, scol2 = st.columns(2)

        with scol1:
            study = select_study(
                'select-study',
                api_client,
                project_name=project_name,
                project_owner=project_owner
            )
        with scol2:
            st.json(study or '{}', expanded=False)
