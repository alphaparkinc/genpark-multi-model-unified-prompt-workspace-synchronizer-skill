from client import MultiModelUnifiedPromptWorkspaceSynchronizerClient

def main():
    client = MultiModelUnifiedPromptWorkspaceSynchronizerClient()
    res = client.synchronize_workspace_deliberation('Design multi-region active-active database replication protocol')
    print('Workspace Session: ' + res['workspace_session_id'] + ' (' + str(res['models_queried_count']) + ' models)')
    print('Diff Matrix: ' + str(res['side_by_side_diff_matrix_rendered']) + ' | Memory Cached: ' + str(res['unified_memory_context_cached']))
    print('Consensus: ' + str(res['cross_model_consensus_rating_pct']) + '%')
    print('Snapshot: ' + res['workspace_snapshot_url'])

if __name__ == '__main__':
    main()
