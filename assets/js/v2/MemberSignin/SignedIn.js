import { Link } from '@reach/router';
import { Divider, Table, Tag } from 'antd';
import React from 'react';

export const SignedIn = ({ members = [] }) => {
  const columns = [
    {
      title: 'Name',
      dataIndex: 'fullName',
      key: 'fullName',
    },
    {
      title: 'Purpose',
      dataIndex: 'purpose',
      key: 'purpose',
    },
    {
      title: 'Signed-in At',
      dataIndex: 'at',
      key: 'at',
      render: v => new Date(v).toLocaleDateString(),
    },
    {
      title: 'Access Status',
      dataIndex: 'status',
      key: 'status',
      render: v =>
        ({
          BANNED: <Tag color="red">{v.toLowerCase()}</Tag>,
          SUSPENDED: <Tag color="yellow">{v.toLowerCase()}</Tag>,
          GOOD: <Tag color="green">{v.toLowerCase()}</Tag>,
        }[v]),
    },
    {
      title: 'Action',
      key: 'action',
      render: v => {
        return (
          <span>
            <Link to={`/members/${v.id}`}>view profile</Link>
            <Divider type="vertical" />
            <a>renew membership</a>
          </span>
        );
      },
    },
  ];
  return <Table rowKey="id" columns={columns} dataSource={members} />;
};
